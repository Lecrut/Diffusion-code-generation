OPERATIONS = {
    'area': lambda s: s * s,
    'perimeter': lambda s: 4 * s
}

def compute_square_metric(side_length, metric_type='area'):
    operation = OPERATIONS.get(metric_type)
    if operation is None:
        raise ValueError(f"Unknown metric type: {metric_type}")
    return operation(side_length)

if __name__ == '__main__':
    side = 15
    area = compute_square_metric(side)
    print(area)