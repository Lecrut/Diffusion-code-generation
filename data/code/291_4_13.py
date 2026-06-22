def compare_yards_inches(y1, i1, y2, i2):
    total_inches_1 = y1 * 36 + i1
    total_inches_2 = y2 * 36 + i2
    
    if total_inches_1 < total_inches_2:
        return f"{y1} yards {i1} inches"
    elif total_inches_2 < total_inches_1:
        return f"{y2} yards {i2} inches"
    else:
        return "Equal"

if __name__ == '__main__':
    result = compare_yards_inches(5, 8, 4, 10)
    print(result)