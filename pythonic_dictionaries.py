# There are two dictionary, e.g.:
# dict_one = {'a': 1, 'b': 2, 'c': 3}
# dict_two = {'d': 1, 'e': 2, 'f': 3, 'a': 99}
# Write a function which returns the merge of the two dictinoary as short as possible e.g.:;
# {'a': 100, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3} 

# another test case:
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_two = {'a': 119, 'b': 258, 'c': 997, 'e': 275,'f': 400, 'g': 950 }
# result = {'a': 120, 'b': 260, 'c': 1000, 'e': 280,'f': 400, 'g': 950 }

def dict_fusion(dict_one, dict_two):

    dict_merge = {}
    for key in dict_one:
        if key in dict_two:
            value_sum = dict_one[key] + dict_two[key]
            dict_merge.update({key: value_sum})
        elif key not in dict_two:
            dict_merge.update({key: dict_one[key]})   
    for key in dict_two:
        if key in dict_one:
            value_sum = dict_one[key] + dict_two[key]
            dict_merge.update({key: value_sum})
        elif key not in dict_one:
            dict_merge.update({key: dict_two[key]})       
    return dict_merge

print(dict_fusion(dict_one, dict_two))