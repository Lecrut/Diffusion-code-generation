def is_valid_member(member):
    return isinstance(member, (int, str))

def contains_target(valid_members, target):
    if not all(is_valid_member(m) for m in valid_members):
        raise ValueError("All members must be integers or strings")
    return any(item == target for item in valid_members)

if __name__ == '__main__':
    valid_members1 = (1, 5, 2, 8, 3)
    target1 = 8
    result1 = contains_target(valid_members1, target1)
    print(f"Does {target1} exist in {valid_members1}? {result1}")

    valid_members2 = ('a', 'b', 'c', 'd')
    target2 = 'z'
    result2 = contains_target(valid_members2, target2)
    print(f"Does {target2} exist in {valid_members2}? {result2}")

    valid_members3 = (10, 20, 30)
    target3 = 25
    result3 = contains_target(valid_members3, target3)
    print(f"Does {target3} exist in {valid_members3}? {result3}")

    valid_members4 = (1, 2, 3)
    target4 = 1
    result4 = contains_target(valid_members4, target4)
    print(f"Does {target4} exist in {valid_members4}? {result4}")