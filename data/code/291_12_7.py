def compare_lengths(feet1, inches1, feet2, inches2):
    total_inches1 = feet1 * 12 + inches1
    total_inches2 = feet2 * 12 + inches2

    if total_inches1 > total_inches2:
        return (feet1, inches1), "feet"
    elif total_inches2 > total_inches1:
        return (feet2, inches2), "feet"
    else:
        rounded_inches = round(total_inches1 / 12) * 12
        feet_result = rounded_inches // 12
        inches_result = rounded_inches % 12
        return (feet_result, inches_result), "feet"

if __name__ == '__main__':
    result1 = compare_lengths(5, 7.5, 3, 9)
    print(f"Longer measurement: {result1[0][0]} feet {result1[0][1]} inches, unit: {result1[1]}")

    result2 = compare_lengths(2, 10, 2, 8)
    print(f"Longer measurement: {result2[0][0]} feet {result2[0][1]} inches, unit: {result2[1]}")