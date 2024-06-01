import statsapi as mlb

score = mlb.boxscore_data(565997)

print(type(score))
print(score)