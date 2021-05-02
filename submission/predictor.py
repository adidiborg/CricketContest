import numpy as np
import pandas as pd
from statistics import mean

def predictRuns(testInput):
    
    prediction = 0
    
    input_match = pd.read_csv(testInput)
    venue = input_match['venue'][0]
    innings = input_match['innings'][0]
    batting_team = input_match['batting_team'][0]
    bowling_team = input_match['bowling_team'][0]
    batsmen = input_match['batsmen'][0]
    bowlers = input_match['bowlers'][0]
    
    matches = pd.read_csv("all_matches_under6.csv")
    
    # venue scores
    
    filter_1 = matches.loc[(matches['venue'] == venue ) & (matches['innings'] == innings )]
    filter_1_match_ids = filter_1.match_id.unique()
    filter_1_runs = []
    
    for i in filter_1_match_ids:
        filter_1_match = filter_1.loc[filter_1['match_id'] == i ]
        filter_1_runs_off_bat = filter_1_match['runs_off_bat'].sum()
        filter_1_runs_extras = filter_1_match['extras'].sum()
        filter_1_total_runs = filter_1_runs_off_bat + filter_1_runs_extras
        filter_1_runs.append(filter_1_total_runs)
    
    filter_1_runs = mean(filter_1_runs)
    try:
        filter_1_runs = mean(filter_1_runs)
    except:
        filter_1_runs = filter_1_runs
    
    # FILTER 2 - batting team score vs bowling team
    
    filter_2 = matches.loc[(matches['batting_team'] == batting_team) & (matches['bowling_team'] == bowling_team) & (matches['innings'] == innings ) ]
    filter_2_match_ids = filter_2.match_id.unique()
    filter_2_runs = []
    
    for i in filter_2_match_ids:
        filter_2_match = filter_2.loc[filter_2['match_id'] == i ]
        filter_2_runs_off_bat = filter_2_match['runs_off_bat'].sum()
        filter_2_runs_extras = filter_2_match['extras'].sum()
        filter_2_total_runs = filter_2_runs_off_bat + filter_2_runs_extras
        filter_2_runs.append(filter_2_total_runs)

    try:
        filter_2_runs = mean(filter_2_runs)
    except:
        filter_2_runs = filter_1_runs
    
    # batting team score vs bowling team at the venue
    
    filter_3 = matches.loc[(matches['venue'] == venue ) & (matches['batting_team'] == batting_team) & (matches['bowling_team'] == bowling_team) & (matches['innings'] == innings ) ]
    filter_3_match_ids = filter_3.match_id.unique()
    filter_3_runs = []
    
    for i in filter_3_match_ids:
        filter_3_match = filter_3.loc[filter_2['match_id'] == i ]
        filter_3_runs_off_bat = filter_3_match['runs_off_bat'].sum()
        filter_3_runs_extras = filter_3_match['extras'].sum()
        filter_3_total_runs = filter_3_runs_off_bat + filter_3_runs_extras
        filter_3_runs.append(filter_3_total_runs)
    
    try:
        filter_3_runs = mean(filter_3_runs)
    except:
        filter_3_runs = filter_1_runs
    
    # batsmen runs at the venue
    
    batsmen = batsmen.split(",")
    filter_4_runs = []
    for i in batsmen:
        filter_4 = matches.loc[(matches['venue'] == venue ) & (matches['striker'] == i ) ]
        filter_4_match_ids = filter_4.match_id.unique()
    
        for j in filter_4_match_ids:
            filter_4_match = filter_1.loc[filter_1['match_id'] == j ]
            filter_4_runs_off_bat = filter_4_match['runs_off_bat'].sum()
            filter_4_runs_extras = filter_4_match['extras'].sum()
            filter_4_total_runs = filter_4_runs_off_bat + filter_4_runs_extras
            filter_4_runs.append(filter_4_total_runs)
            
    try:
        filter_4_runs = mean(filter_4_runs)
    except:
        filter_4_runs = filter_1_runs
    
    # bowler runs given at the venue
    bowlers = bowlers.split(",")
    filter_5_runs = []
    for i in bowlers:
        filter_5 = matches.loc[(matches['venue'] == venue ) & (matches['bowler'] == i ) ]
        filter_5_match_ids = filter_5.match_id.unique()
    
        for j in filter_5_match_ids:
            filter_5_match = filter_1.loc[filter_1['match_id'] == j ]
            filter_5_runs_off_bat = filter_5_match['runs_off_bat'].sum()
            filter_5_runs_extras = filter_5_match['extras'].sum()
            filter_5_total_runs = filter_5_runs_off_bat + filter_5_runs_extras
            filter_5_runs.append(filter_5_total_runs)

    try:
        filter_5_runs = mean(filter_5_runs)
    except:
        filter_5_runs = filter_1_runs
    
    prediction = round((filter_1_runs+filter_2_runs+filter_3_runs+filter_4_runs+filter_5_runs)/5)
    
    
    return prediction