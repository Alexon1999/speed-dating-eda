def get_value(dataframe, idx_variable, target_variable):
    target = dataframe.loc[(dataframe['iid'] == idx_variable), target_variable]
    if target.values.shape[0] == 0:
        return 18
    return target.values[0]
