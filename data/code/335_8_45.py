def split_string(s: str, delimiter: str) -> list[str]:
    return [part for part in s.split(delimiter)]
if __name__ == '__main__':
    test_str = "apple;banana;cherry"
    delimiters_to_test = [";", ","]
    results = {}
    result_semi = split_string(test_str, ";")
    results["semicolon"] = {
        "input": test_str,
        "delimiter": ";",
        "output": result_semi
    }
    result_comma = split_string("apple;banana,cherry", ",")
    results["comma"] = {
        "input": "apple;banana,cherry",
        "delimiter": ",",
        "output": result_comma
    }
    print(results)