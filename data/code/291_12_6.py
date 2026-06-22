def compare_measurements(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2
    if total_inches1 > total_inches2:
        return (feet1, inches1)
    elif total_inches2 > total_inches1:
        return (feet2, inches2)
    else:
        return None
if __name__ == '__main__':
    result = compare_measurements(5, 6.75, 4, 9.25)
    print(result)