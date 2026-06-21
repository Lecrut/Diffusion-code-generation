def segment_by_sign(tuples):
    result = {True: [], False: []}
    for item, value in tuples:
        sign = value > 0
        result[sign].append(item)
    return result

if __name__ == '__main__':
    data = [(-3, -1), (4, 2), (-5, -2), (6, 3), (-7, -4)]
    segmented_data = segment_by_sign(data)
    print(segmented_data)