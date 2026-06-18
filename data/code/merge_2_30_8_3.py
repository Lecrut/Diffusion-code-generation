import json
def process_data(records):
    aggregated = {}
    preserved_records = []
    for record in records:
        category = record.get('category', 'unknown')
        value = record.get('value', 0)
        if category not in aggregated:
            aggregated[category] = {'count': 0, 'sum': 0}
        aggregated[category]['count'] += 1
        aggregated[category]['sum'] += value
        preserved_records.append({
            'id': record['id'],
            'value': value,
            'metadata': record.get('metadata', {}),
            'aggregated_count': None,
            'aggregated_sum': None
        })
    for category in aggregated:
        count = aggregated[category]['count']
        sum_val = aggregated[category]['sum']
        for i, rec in enumerate(preserved_records):
            if record_id := [r['id'] for r in preserved_records][i]:                                                                                          
                pass
    return list(aggregated.values()), preserved_records
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10, 'category': 'electronics', 'metadata': {'brand': 'A'}},
        {'id': 2, 'value': 25, 'category': 'clothing', 'metadata': {'size': 'M'}},
        {'id': 3, 'value': 15, 'category': 'electronics', 'metadata': {'model': 'X'}},
        {'id': 4, 'value': 80, 'category': 'home', 'metadata': {}},
    ]
    aggregates, final_list = process_data(sample_data)
    print("Aggregated Data:")
    for cat in aggregates:
        print(f"{cat['count']} items, Total Value: {cat['sum']}")
    print("\nPreserved Records with Aggregation Status:")
    id_map = {}
    for r in sample_data:
        id_map[r['id']] = r.get('category')
    final_output_list = []
    agg_dict_final = {cat[0]: cat} if isinstance(cat, list) else dict(aggregates)                     
    temp_agg = {}
    for r in sample_data:
        c = r['category']
        if c not in temp_agg:
            temp_agg[c] = {'count': 0, 'sum': 0}
        temp_agg[c]['count'] += 1
        temp_agg[c]['sum'] += r['value']
    for i, item in enumerate(sample_data):
        cat = item['category']
        count = temp_agg[cat]['count']
        total = temp_agg[cat]['sum']
        final_output_list.append({
            'id': item['id'],
            'original_value': item['value'],
            'metadata': item.get('metadata', {}),
            'aggregated_count': count,
            'aggregated_sum': total
        })
    print("\nFinal Output List:")
    for i in range(len(final_output_list)):
        print(f"ID {final_output_list[i]['id']}: Count={final_output_list[i]['aggregated_count']}, Sum={final_output_list[i]['aggregated_sum']}")