def analyze_multiples(numbers):
    for num in numbers:
        if num % 3 == 0 or num % 5 == 0:
            return True
    return False
if __name__ == '__main__':
    set1 = [1, 2, 4, 7, 8]
    set2 = [3, 5, 6, 10, 11]
    set3 = [10, 15, 20, 25]
    set4 = [1, 2, 3, 4, 5]
    print(f"Set {set1}: {analyze_multiples(set1)}")
    print(f"Set {set2}: {analyze_multiples(set2)}")
    print(f"Set {set3}: {analyze_multiples(set3)}")
    print(f"Set {set4}: {analyze_multiples(set4)}")