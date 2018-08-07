#Q1. Given List
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#Do this by using slicing from the front (positive)
#Do this by using slicing from the back (negative)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print "slicing from the front:",x[7:12] #slicing from  the front (positive)
print "slicing from the back:", x[-9:-4]#slicing from the back(negative)

#Q2. Print even numbers from the list by list slicing

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print "even numbers are:",y[1:][::2]#prints only even number slicing function '[1:]' will start from the 1 index
#and [::2] is used for interval

#Q3. Printing everyfourth number from the list
#  z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print (z[0:][::4]) #prints every fourth number



