import numpy as np
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])
# Accessing elements
if True:
    print (ridership[1, 3])
    print (ridership[1:3, 3:5])
    print (ridership[1, :])

    print("output",ridership[1:4])

output:
2328
[[2328 2539]
 [6461 2691]]
[1478 3877 3674 2328 2539]
output [1:4] [[1478 3877 3674 2328 2539]
 [1613 4088 3991 6461 2691]
 [1560 3392 3826 4787 2613]]

# Vectorized operations on rows or columns
if True:
    print (ridership[0, :] + ridership[1, :])
    print (ridership[:, 0] + ridership[:, 1])

output:
[1478 3877 3676 2333 2539]
[   0 5355 5701 4952 6410 5509  324    2 5223 5385]

# Vectorized operations on entire arrays
if True:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print (a + b)


find the station with maximum ridersfirst daya
max_station = ridership[0,:].argmax()
print (max_station)

#find the mean riders per day for that station 
mean_for_max = ridership[:,max_station].mean()
print (mean_for_max)
# #find the mean ridership overall

overall_mean = ridership.mean()
print (overall_mean)


# NumPy axis argument
if True:
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
print (a.sum())
print (a.sum(axis=0))#(1+4+7)
print (a.sum(axis=1))#(1+2+3)

output:
45
[12 15 18]
[ 6 15 24]
