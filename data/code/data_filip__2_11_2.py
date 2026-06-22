def check_palindrome_status(sequence):
    lower_seq = sequence.lower()
    left = 0
    right = len(lower_seq) - 1
    while left < right:
        if lower_seq[left] != lower_seq[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    items = ['racecar', 'hello', 'Madam', '12321', 'Able was I ere I saw Elba']
    for item in items:
        print(check_palindrome_status(item))