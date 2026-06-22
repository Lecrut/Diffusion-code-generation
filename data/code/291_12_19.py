def compare_measurements(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2
    if total_inches1 > total_inches2:
        return (feet1, inches1, 'feet')
    elif total_inches2 > total_inches1:
        return (feet2, inches2, 'feet')
    else:
        rounded_inches = round(total_inches1)
        feet = rounded_inches // 12
        inches = rounded_inches % 12
        return (feet, inches, 'inches')
if __name__ == '__main__':
    result = compare_measurements(5, 7.5, 4, 10)
    print(result)