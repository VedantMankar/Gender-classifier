from sklearn import tree

cls = tree.DecisionTreeClassifier()

#[HEIGHT,WEIGHT,SHOE SIZE]
X = [[181, 80, 10], [177, 70, 8], [160, 60, 7], [154, 54, 8], [166, 65, 9],
     [190, 90, 10], [175, 64, 9],
     [177, 70, 8], [159, 55, 7], [171, 75, 8], [181, 85, 10],[190,88,9],[185,79,8]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Training our data
cls = cls.fit(X,Y)
HWS = []
#taking data
h = input("Enter Height: ")
HWS.append(h)
w = input("Enter weight: ")
HWS.append(w)
s = input("ENter shoe-size: ")
HWS.append(s)

prediction = cls.predict([HWS])
print(prediction)


