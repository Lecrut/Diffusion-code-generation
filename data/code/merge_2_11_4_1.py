import pandas as pd
def detect_uniform_rows(dataframe):
    result = []
    for index, row in dataframe.iterrows():
        clean_values = [x for x in row if pd.notna(x)]
        if not clean_values:
            result.append({
                'row_index': index,
                'is_uniform': False,
                'reason': 'No non-null values found'
            })
            continue
        try:
            numeric_values = [float(x) if x != '' else None for x in clean_values]
            unique_count = len(set(numeric_values))
            is_uniform = (unique_count == 1 and not any(pd.isna(v) for v in numeric_values))
            result.append({
                'row_index': index,
                'is_uniform': is_uniform,
                'value' if is_uniform else None: numeric_values[0] if is_uniform or unique_count > 1 else None,
                'reason': f'Detected {unique_count} unique values' if not is_uniform and unique_count == len(set(clean_values)) else (f'Single value detected: {numeric_values[0]}' if is_uniform else '')
            })
        except ValueError:
            result.append({
                'row_index': index,
                'is_uniform': False,
                'reason': 'Non-convertible data type found'
            })
    return pd.DataFrame(result)
if __name__ == '__main__':
    sample_data = [
        ['A', 10.0],
        ['B', None],
        [],
        ['C', 20.0, '30'],
        ['D', 50.0, 50.0, 60.0]
    ]
    df = pd.DataFrame(sample_data)
    uniform_analysis = detect_uniform_rows(df)
    print(uniform_analysis.to_string())