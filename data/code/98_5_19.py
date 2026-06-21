def evaluate_subscription_records(records):
    status_map = {'active': 'Active', 'premium': 'Premium', 'expired': 'Expired'}
    evaluated_records = []
    for record in records:
        current_status = record.get('status', 'unknown')
        if current_status == 'premium':
            final_label = 'Premium'
        elif current_status == 'expired':
            final_label = 'Expired'
        elif current_status == 'active':
            final_label = 'Active'
        else:
            final_label = 'Unknown'
        new_record = dict(record)
        new_record['evaluation_result'] = final_label
        evaluated_records.append(new_record)
    return evaluated_records

if __name__ == '__main__':
    sample_records = [
        {'id': 101, 'status': 'active', 'name': 'Alice'},
        {'id': 102, 'status': 'premium', 'name': 'Bob'},
        {'id': 103, 'status': 'expired', 'name': 'Charlie'},
        {'id': 104, 'status': 'inactive', 'name': 'Diana'}
    ]
    output = evaluate_subscription_records(sample_records)
    print(output)