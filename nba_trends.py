import pandas
import matplotlib.pyplot as plt

nba_csv = pandas.read_csv('all_seasons.csv')
num_rows = len(nba_csv)

def fn_scoring():
    scoring_dict = {}

    for x in range(num_rows):
        curr_row = nba_csv.loc[x]

        curr_player_name= curr_row['player_name'].split()[0]
        
        curr_player_pts = curr_row['pts']
        curr_player_gp = curr_row['gp']
        curr_player_tot_pts = round(curr_player_pts * curr_player_gp)

        if curr_player_name in scoring_dict:
            scoring_dict[curr_player_name] += curr_player_tot_pts
        else:
            scoring_dict[curr_player_name] = curr_player_tot_pts
    
    sorted_scoring_dict = sorted(scoring_dict.items(), key=lambda x:x[1], reverse=True)

    top_10_players = sorted_scoring_dict[:10]
    top_players, top_pts = zip(*top_10_players)

    plt.bar(top_players, top_pts)
    
    plt.xlabel('First Names')
    plt.ylabel('Total Points')
    plt.title('Most points by first names from 1996-2021')

    plt.show()

fn_scoring()