import random
def play_game(score, health, level):
    if health <= 0:
        return "Game Over: You ran out of health."
    elif score >= 100 and level >= 3:
        return "Victory! You achieved a perfect score and high level."
    elif score >= 50:
        return "Success! You reached a good score."
    elif health > 20:
        return "Partial Success. Keep trying."
    else:
        return "Failure. You need more effort."
if __name__ == '__main__':
    sample_score = 75
    sample_health = 30
    sample_level = 2
    result = play_game(sample_score, sample_health, sample_level)
    print(result)