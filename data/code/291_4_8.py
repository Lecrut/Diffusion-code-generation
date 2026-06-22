def compare_measures(yards1, inches1, yards2, inches2):
    if not all(isinstance(x, (int, float)) for x in [yards1, inches1, yards2, inches2]):
        raise ValueError("All inputs must be numbers.")
    
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    
    if total_inches1 < total_inches2:
        return f"{yards1} yards {inches1} inches"
    elif total_inches2 < total_inches1:
        return f"{yards2} yards {inches2} inches"
    else:
        return "Both measures are equal."

if __name__ == '__main__':
    shorter_measure = compare_measures(5, 7, 4, 8)
    print(shorter_measure)