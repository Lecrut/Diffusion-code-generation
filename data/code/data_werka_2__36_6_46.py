def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = {
        "hello": {"recursive": None, "slicing": None},
        "world": {"recursive": None, "slicing": None},
        "python": {"recursive": None, "slicing": None}
    }

    for string, results in sample_strings.items():
        results["recursive"] = reverse_string_recursive(string)
        results["slicing"] = reverse_string_slicing(string)

    for string, results in sample_strings.items():
        print(f"Original: {string}")
        print(f"Reversed by recursion: {results['recursive']}")
        print(f"Reversed by slicing: {results['slicing']}")