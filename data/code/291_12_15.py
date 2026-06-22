def compare_feet_inches(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2
    
    if total_inches1 > total_inches2:
        return (total_inches1 / 12, "feet")
    elif total_inches2 > total_inches1:
        return (total_inches2 / 12, "feet")
    else:
        return (round((total_inches1 + total_inches2) / 24), "inches")

if __name__ == '__main__':
    print(compare_feet_inches(5, 6.7, 3, 9.2))
    print(compare_feet_inches(2, 0, 2, 0))
    print(compare_feet_inches(1, 11, 1, 11))