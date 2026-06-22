def compare_measures(yards1, inches1, yards2, inches2):
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    if total_inches1 < total_inches2:
        return f"{yards1} yards {inches1} inches"
    elif total_inches2 < total_inches1:
        return f"{yards2} yards {inches2} inches"
    else:
        return "Equal measures"

if __name__ == '__main__':
    result = compare_measures(5, 8, 4, 36)
    print(result)