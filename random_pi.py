#zero hour problem 3-11-24 9:38 PM Revath Sankar


import random, math, tqdm, matplotlib.pyplot, matplotlib.patches

class PiEstimator:
    def __init__(self, n:int = 100) -> None:
        self.n = n
        self.points = []
        self.circle_point_count = 0


    def generate_random_points(self)->None:
        for _ in range(self.n):
            x,y = random.random(), random.random()
            self.points.append([x,y])
    def distance(self,point1, point2)->float:
        return math.dist(point1, point2)

    def count_circle_points(self)->int:
        count = 0
        for idx, point in tqdm.tqdm(enumerate(self.points)):
            if self.distance([0,0], point) <= 1:
                count += 1
        self.circle_point_count = count
        return count

    def get_approx_pi(self)->float:
        return 4 * ((self.circle_point_count)/self.n)
    def visualize(self)->None:
        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]
        fig, ax = matplotlib.pyplot.subplots()
        fig.suptitle(f"Plotting of Randomized Points to Estimate Pi | Points Plotted {self.n} | Estimation: {self.get_approx_pi()}")
        ax.scatter(x,y)
        circle = matplotlib.pyplot.Circle((0,0),1, color='g', fill = False)
        ax.set_aspect('equal', adjustable = 'datalim')
        ax.add_patch(circle)
        matplotlib.pyplot.show()


if __name__ == '__main__':
    nums = int(input("Please enter the integer number of points you would like to generate.\n"))
    pi = PiEstimator(nums)
    pi.generate_random_points()
    print(f"Number of Points within Circle: {pi.count_circle_points()}")
    print(f"Approximate Value of Pi at {pi.n} parameters {pi.get_approx_pi()}")
    pi.visualize()
