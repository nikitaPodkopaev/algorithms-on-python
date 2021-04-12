import math


def get_min_value(ribs,tops):
    minrib = (math.inf, -1, -1)

    for top in tops:
        min_rib_value = min(ribs, key=lambda x: x[0] if (x[1] == top or x[2] == top) and (x[1] not in tops or x[2] not in tops) else math.inf)
        if minrib[0] > min_rib_value[0]:
            minrib = min_rib_value
    return minrib

ribs = [(math.inf, -1, -1), (10, 1, 2), (4, 1, 3), (8, 1, 4), (11, 1, 5), (7, 1, 6), (15, 2, 3), (40, 2, 5), (33, 3, 4), (51, 4, 6)]

number_of_tops = 6
connected_tops = {1}
connected_tops_values = []

while len(connected_tops) < number_of_tops:
    min_rib = get_min_value(ribs, connected_tops)
    if min_rib[0] == math.inf:
        break

    connected_tops_values.append(min_rib)
    connected_tops.add(min_rib[1])
    connected_tops.add(min_rib[2])
print(connected_tops_values)
