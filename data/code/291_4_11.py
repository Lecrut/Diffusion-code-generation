unit_conversion = {'inches': 36}

def compare_measures(yards1, inches1, yards2, inches2):
    total_inches1 = yards1 * unit_conversion['inches'] + inches1
    total_inches2 = yards2 * unit_conversion['inches'] + inches2
    if total_inches1 < total_inches2:
        return f"{yards1} yards {inches1} inches"
    else:
        return f"{yards2} yards {inches2} inches"

if __name__ == '__main__':
    result = compare_measures(5, 3, 4, 10)
    print(result)