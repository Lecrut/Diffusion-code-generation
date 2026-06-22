def compare_measures(inches1, feet1, inches2, feet2):
    total_inches1 = inches1 + feet1 * 12
    total_inches2 = inches2 + feet2 * 12
    
    if total_inches1 > total_inches2:
        return f"{inches1} inches and {feet1} feet"
    else:
        return f"{inches2} inches and {feet2} feet"

if __name__ == '__main__':
    print(compare_measures(36, 0, 48, 0))