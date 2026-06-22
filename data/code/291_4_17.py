def compare_measures(yards1, inches1, yards2, inches2):
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    
    if total_inches1 < total_inches2:
        return f"{yards1} yards and {inches1} inches"
    elif total_inches1 > total_inches2:
        return f"{yards2} yards and {inches2} inches"
    else:
        return "Equal measures"

if __name__ == '__main__':
    shorter_measure = compare_measures(3, 5, 2, 10)
    print(shorter_measure)