CHARACTER_STATUS = {"seen": 1, "repeated": 2}

def find_repeated_characters(text):
    char_tracker = {}
    for char in text:
        status = char_tracker.get(char, 0)
        if status == 0:
            char_tracker[char] = CHARACTER_STATUS["seen"]
        elif status == CHARACTER_STATUS["seen"]:
            char_tracker[char] = CHARACTER_STATUS["repeated"]
    second_pass_tracker = set()
    for char in text:
        if char_tracker.get(char) == CHARACTER_STATUS["repeated"]:
            second_pass_tracker.add(char)
    return sorted(list(second_pass_tracker))

if __name__ == '__main__':
    test_input = "banana"
    result = find_repeated_characters(test_input)
    print(result)