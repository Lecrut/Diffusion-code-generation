if __name__ == '__main__':
    score = 0
    level = 1
    item_found = False
    is_lucky = False
    if level == 1:
        if score < 10:
            if item_found:
                score += 5
            else:
                score += 2
        else:
            score += 10
    elif level == 2:
        if score > 15:
            if item_found:
                score += 15
            else:
                score += 10
        else:
            score += 5
    else:
        if item_found:
            score += 20
        else:
            score += 10
    if score > 25:
        is_lucky = True
    elif score >= 15:
        is_lucky = False
    else:
        is_lucky = False
    print(f"Final Score: {score}")
    print(f"Is Lucky: {is_lucky}")