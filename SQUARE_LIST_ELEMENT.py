#output : square of each element in the list
#logic : Multiply each element with itself and append in the list . use of two list . one for input , one for output . o(n) complexity.


def squarelist(li):
    squared_list = []

    for i in range(0, len(li)):
        result = li[i] * li[i]
        squared_list.append(result)

    return squared_list


li = [10, 2, 5, 7, 9, 15]
print("original list", li)
print("squared list ", squarelist(li))
