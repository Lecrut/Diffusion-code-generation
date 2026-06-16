def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    string1 = "abc"
    count1 = 5
    result1 = repeat_action(string1, count1)
    print(f"Input string: {string1}, Repetitions: {count1}")
    print(f"Result: {result1}")
    string2 = "hello"
    count2 = 1000000
    result2 = repeat_action(string2, count2)
    print(f"Input string: {string2}, Repetitions: {count2}")
    print(f"Result length: {len(result2)}")