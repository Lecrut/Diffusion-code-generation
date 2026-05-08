import random
def play_game(level, score):
    if level == 1:
        if score > 5:
            return "Level 1 Success"
        else:
            return "Level 1 Failure"
    elif level == 2:
        if score >= 10:
            return "Level 2 Success"
        elif score > 5:
            return "Level 2 Partial Success"
        else:
            return "Level 2 Failure"
    else:
        if score > 15:
            return "Level 3 Bonus"
        else:
            return "Level 3 Standard"
if __name__ == '__main__':
    game_level = 2
    game_score = 12
    result = play_game(game_level, game_score)
    print(result)