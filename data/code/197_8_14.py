def is_valid_member(member):
    return isinstance(member, (int, str))

def contains_target(valid_members, target):
    if not all(is_valid_member(m) for m in valid_members):
        raise ValueError("All members must be integers or strings")
    return any(item == target for item in valid_members)

if __name__ == '__main__':
    valid_members = (1, 'a', 2, 'b', 3)
    target1 = 2
    result1 = contains_target(valid_members, target1)
    print(f"Does {target1} exist in {valid_members}? {result1}")

    target2 = 'c'
    result2 = contains_target(valid_members, target2)
    print(f"Does {target2} exist in {valid_members}? {result2}")

    target3 = 4
    try:
        result3 = contains_target(valid_members, target3)
    except ValueError as e:
        print(e)