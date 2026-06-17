import json
def aggregate_item_counts(sources):
    aggregated = {}
    for source in sources:
        if isinstance(source, dict) and 'items' in source:
            items_data = source['items']
            if isinstance(items_data, list):
                for item_entry in items_data:
                    if isinstance(item_entry, (dict, int)):
                        key = str(item_entry).replace(' ', '_')
                        aggregated[key] = 1
    return aggregated
def main():
    sample_sources = [
        {
            'source_name': 'Source A',
            'items': [{'id': 1}, {'id': 2}]
        },
        {
            'source_name': 'Source B',
            'items': [{'id': 3}, {'id': 4}]
        }
    ]
    result = aggregate_item_counts(sample_sources)
    output_json = json.dumps(result, indent=2)
    print(output_json)
if __name__ == '__main__':
    main()