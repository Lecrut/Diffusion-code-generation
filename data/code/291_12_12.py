def compare_measurements(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2
    
    if total_inches1 > total_inches2:
        return (feet1, inches1)
    elif total_inches2 > total_inches1:
        return (feet2, inches2)
    else:
        return (feet1, inches1)

if __name__ == '__main__':
    print(compare_measurements(5, 6.5, 4, 9))