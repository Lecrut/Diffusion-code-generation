if __name__ == '__main__':
    score = 0
    level = 1
    item_a = "apple"
    item_b = "banana"
    if level == 1:
        if score < 10:
            if item_a == "apple":
                score += 5
                level = 2
            elif item_b == "banana":
                score += 3
        else:
            if score < 20:
                score += 10
            else:
                score += 20
    elif level == 2:
        if score > 15:
            if item_a == "apple":
                score += 15
            elif item_b == "banana":
                score += 10
        else:
            if score < 5:
                score += 5
            else:
                score += 1
    else:
        if score > 30:
            score += 50
        else:
            score += 10
    print(f"Final Score: {score}")