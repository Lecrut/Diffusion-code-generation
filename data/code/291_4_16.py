def compare_lengths(yards1, inches1, yards2, inches2):
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    if total_inches1 < total_inches2:
        return f"{yards1} yards {inches1} inches"
    elif total_inches2 < total_inches1:
        return f"{yards2} yards {inches2} inches"
    else:
        return "Equal lengths"

if __name__ == '__main__':
    sample_yards1, sample_inches1 = 5, 8
    sample_yards2, sample_inches2 = 4, 30
    result = compare_lengths(sample_yards1, sample_inches1, sample_yards2, sample_inches2)
    print(result)