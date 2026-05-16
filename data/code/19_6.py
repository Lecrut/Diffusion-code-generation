def decide_truth(val1, val2):
    return val1 == val2
if __name__ == '__main__':
    result1 = decide_truth(5, 5)
    print(f"decide_truth(5, 5): {result1}")
    result2 = decide_truth(10, 3)
    print(f"decide_truth(10, 3): {result2}")
    result3 = decide_truth("hello", "hello")
    print(f"decide_truth(\"hello\", \"hello\"): {result3}")
    result4 = decide_truth(True, False)
    print(f"decide_truth(True, False): {result4}")