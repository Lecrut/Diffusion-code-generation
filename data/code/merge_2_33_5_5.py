def main():
    name_set = {"Alice", "Bob", "Charlie", "David"}
    test_names = ["Eve", "Frank", "Grace"]
    found_count = 0
    for name in test_names:
        if name in name_set:
            print(f"Found: {name}")
            found_count += 1
    print(f"\nTotal matches: {found_count}/3")
if __name__ == '__main__':
    main()