import copy

class PolygonRepeater:
    @staticmethod
    def deep_copy_and_repeat(polygon_dict, multiplier):
        return [copy.deepcopy(polygon_dict) for _ in range(multiplier)]

if __name__ == '__main__':
    sample_polygon = {'vertices': [(0, 0), (1, 0), (1, 1)], 'color': 'green'}
    multiplier = 3
    result = PolygonRepeater.deep_copy_and_repeat(sample_polygon, multiplier)
    print(result)