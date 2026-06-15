def create_membership_structure(lists):
    membership_dict = {}
    for key, value in lists.items():
        if key not in membership_dict:
            membership_dict[key] = set()
        membership_dict[key].update(value)
    return membership_dict
if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'date', 'elderberry']
    list3 = ['fig', 'grape', 'apple']
    all_lists = {
        'group_a': list1,
        'group_b': list2,
        'group_c': list3
    }
    membership_store = create_membership_structure(all_lists)
    print("Membership Store:")
    print(membership_store)
    print("\nFast Lookups:")
    item1 = 'banana'
    print(f"Is '{item1}' a member? {'Yes' if item1 in membership_store else 'No'}")
    item2 = 'apple'
    print(f"Is '{item2}' a member? {'Yes' if item2 in membership_store else 'No'}")
    item3 = 'kiwi'
    print(f"Is '{item3}' a member? {'Yes' if item3 in membership_store else 'No'}")