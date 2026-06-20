import argparse

def convert_distance(value, from_unit, to_unit):
    m_per_unit = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if from_unit not in m_per_unit:
        raise ValueError(f"Invalid input unit: {from_unit}")
    if to_unit not in m_per_unit:
        raise ValueError(f"Invalid output unit: {to_unit}")
    
    meters = value * m_per_unit[from_unit]
    return meters / m_per_unit[to_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert distance between units.')
    parser.add_argument('distance', type=float, help='The distance value to convert.')
    parser.add_argument('from_unit', type=str, help='The unit of the input distance.')
    parser.add_argument('to_unit', type=str, help='The desired output unit.')
    
    args = parser.parse_args([])
    args = argparse.Namespace(distance=10, from_unit='km', to_unit='mi')
    
    result = convert_distance(args.distance, args.from_unit, args.to_unit)
    print(result)