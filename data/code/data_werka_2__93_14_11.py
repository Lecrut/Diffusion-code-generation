def both_flags_false(flag_one, flag_two):
    lookup_table = {True: True, False: False}
    status_one = lookup_table.get(flag_one, False)
    status_two = lookup_table.get(flag_two, False)
    return not status_one and not status_two

if __name__ == '__main__':
    sample_first = False
    sample_second = False
    computed_result = both_flags_false(sample_first, sample_second)
    print(computed_result)