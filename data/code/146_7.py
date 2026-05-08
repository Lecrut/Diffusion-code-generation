import random
def play_game(level, score, health):
    if level == 1:
        if score > 5 and health > 10:
            return "Victory"
        elif score > 0:
            return "Partial Win"
        else:
            return "Defeat"
    elif level == 2:
        if score >= 10 and health > 5:
            return "Great Success"
        elif score >= 5:
            return "Moderate Success"
        else:
            return "Failure"
    else:
        if score > 20:
            return "Epic Win"
        elif score > 10:
            return "Good Game"
        else:
            return "Game Over"
if __name__ == '__main__':
    level_val = 2
    score_val = 12
    health_val = 15
    result = play_game(level_val, score_val, health_val)
    print(result)