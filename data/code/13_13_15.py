def snake_to_camel(s):
    return "".join(word.capitalize() if i else word for i, word in enumerate(s.split("_")))

if __name__ == "__main__":
    test_cases = ["user_name", "first_name", "api_key", "max_retry_count", "single"]
    results = [snake_to_camel(case) for case in test_cases]
    for original, converted in zip(test_cases, results):
        print(f"{original} -> {converted}")