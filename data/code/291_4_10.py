def validate_input(yards1, inches1, yards2, inches2):
    if not (isinstance(yards1, int) and isinstance(inches1, int)):
        raise ValueError("Yards and inches must be integers.")
    if not (isinstance(yards2, int) and isinstance(inches2, int)):
        raise ValueError("Yards and inches must be integers.")

def compare_measures(yards1, inches1, yards2, inches2):
    validate_input(yards1, inches1, yards2, inches2)
    
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    
    if total_inches1 < total_inches2:
        return (yards1, inches1, 'yards')
    elif total_inches1 > total_inches2:
        return (yards2, inches2, 'yards')
    else:
        return (yards1, inches1, 'inches')

if __name__ == '__main__':
    result = compare_measures(5, 8, 4, 12)
    print(result)