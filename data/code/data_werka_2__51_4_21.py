def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment) * 2

if __name__ == '__main__':
    sample_segments = [
        {'length1': 3, 'length2': 4},
        {'length1': 5, 'length2': 12},
        {'length1': 7, 'length2': 24}
    ]
    
    lengths_map = {
        'segment1': [sample_segments[0]['length1'], sample_segments[0]['length2']],
        'segment2': [sample_segments[1]['length1'], sample_segments[1]['length2']],
        'segment3': [sample_segments[2]['length1'], sample_segments[2]['length2']]
    }
    
    for key, lengths in lengths_map.items():
        perimeter = next(perimeter_generator([lengths]))
        print(f"Perimeter of {key}: {perimeter}")