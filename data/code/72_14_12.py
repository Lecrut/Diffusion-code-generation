def compute_position_matches(primary, secondary, lookup_table):
    match_count = 0
    for label, index in lookup_table.items():
        if index >= 0 and index < len(primary) and index < len(secondary):
            if primary[index] == secondary[index]:
                match_count += 1
    return match_count

if __name__ == '__main__':
    array_x = [7, 8, 9, 10, 11]
    array_y = [7, 8, 99, 10, 11]
    position_labels = {
        'start': 0,
        'middle': 2,
        'end': 4
    }
    total_matches = compute_position_matches(array_x, array_y, position_labels)
    print(total_matches)