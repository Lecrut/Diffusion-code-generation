def compare_values(v1, v2):
    return v1 == v2
if __name__ == '__main__':
    print(f"compare_values(10, 10): {compare_values(10, 10)}")
    print(f"compare_values(5, 3): {compare_values(5, 3)}")
    print(f"compare_values('a', 'a'): {compare_values('a', 'a')}")
    print(f"compare_values(True, True): {compare_values(True, True)}")
    print(f"compare_values(1.5, 1.5): {compare_values(1.5, 1.5)}")
    print(f"compare_values(1, 2): {compare_values(1, 2)}")