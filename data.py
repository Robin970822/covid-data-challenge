feature = [
    'Age',
    'Sex',
    'Temp_C',
    'Cough',
    'DifficultyInBreathing',
    'WBC',
    'CRP',
    'Fibrinogen',
    'LDH',
    'Ddimer',
    'Ox_percentage',
    'PaO2',
    'SaO2',
    'pH',
    'CardiovascularDisease',
    'RespiratoryFailure',
]

binary_feature = [
    'Sex',
    'Cough',
    'DifficultyInBreathing',
    'CardiovascularDisease',
    'RespiratoryFailure',
]

mean = [64.44, 0.34, 37.60, 0.51, 0.50, 7.06, 40.68, 602.52,
        368.17, 2.5e3, 92.54, 72.09, 91.92, 7.45, 0.28, 0.02]
std = [15.05, 0.34 * (1 - 0.34), 0.97, 0.51 * (1 - 0.51), 0.50 * (1 - 0.50), 3.53, 66.93,
       158.36, 235.22, 6743.13, 7.00, 26.11, 8.24, 0.06, 0.28 * (1 - 0.28), 0.02 * (1 - 0.02)]


def fill_dataset(dataset, feature, filled_feature, save_path):
    filled_dataset = dataset.copy()
    filled_dataset[feature] = filled_feature
    for f in binary_feature:
        filled_dataset[f] = filled_dataset[f].map(get_binary)
    filled_dataset.to_csv(save_path, index=None)
    return filled_dataset


def get_severity(Prognosis):
    if Prognosis == 'MILD':
        return 0
    elif Prognosis == 'SEVERE':
        return 1


def get_binary(data, thres=0.5):
    return int(data > thres)


def z_score_normalize(X, mean=mean, std=std):
    return (X - mean) / std


def z_score_denormalize(X, mean=mean, std=std):
    return (X * std) + mean
