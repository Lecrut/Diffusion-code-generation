def compare_strings(s1: str, s2: str) -> bool:
    return s1 == s2
if __name__ == '__main__':
    print(f"compare_strings('hello', 'hello'): {compare_strings('hello', 'hello')}")
    print(f"compare_strings('hello', 'world'): {compare_strings('hello', 'world')}")
    print(f"compare_strings('', ''): {compare_strings('', '')}")
    print(f"compare_strings('', ''): {compare_strings('', '')}")
    print(f"compare_strings('a', 'a'): {compare_strings('a', 'a')}")
    print(f"compare_strings('a', 'b'): {compare_strings('a', 'b')}")
    print(f"compare_strings('abc', 'abc'): {compare_strings('abc', 'abc')}")
    print(f"compare_strings('abc', 'abd'): {compare_strings('abc', 'abd')}")
    print(f"compare_strings('', 'a'): {compare_strings('', 'a')}")
    print(f"compare_strings(' ', ' '): {compare_strings(' ', ' ')}")