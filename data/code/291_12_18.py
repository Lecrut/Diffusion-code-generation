def compare_lengths(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2
    
    if total_inches1 > total_inches2:
        return (total_inches1 / 12, "feet")
    elif total_inches2 > total_inches1:
        return (total_inches2 / 12, "feet")
    else:
        return (round(total_inches1 / 12), "feet")

if __name__ == '__main__':
    result = compare_lengths(5, 3.75, 4, 9)
    print(result)