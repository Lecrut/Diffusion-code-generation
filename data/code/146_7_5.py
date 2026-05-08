import random
def play_game(score, health, level):
    if health <= 0:
        return "Game Over: You ran out of health."
    elif score >= 100 and level >= 3:
        return "Victory! You achieved a perfect score and high level."
    elif score >= 50:
        return "Good job! You reached a decent score."
    elif health > 20:
        return "You are doing okay, but need more focus."
    else:
        return "Keep trying! You are in trouble."
if __name__ == '__main__':
    sample_score = 75
    sample_health = 35
    sample_level = 2
    result = play_game(sample_score, sample_health, sample_level)
    print(result)