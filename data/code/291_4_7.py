def compare_lengths(yards1, inches1, yards2, inches2):
    total_inches1 = yards1 * 36 + inches1
    total_inches2 = yards2 * 36 + inches2
    if total_inches1 < total_inches2:
        return f"{yards1} yards {inches1} inches"
    else:
        return f"{yards2} yards {inches2} inches"

if __name__ == '__main__':
    print(compare_lengths(5, 0, 4, 36))