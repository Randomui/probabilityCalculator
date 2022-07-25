import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **items):
        self.contents = []
        for key,value in items.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self,number):
        try:
            draw_list = random.sample(self.contents, number)            #crea lista random de items
        except:
            draw_list = copy.deepcopy(self.contents)                    #si falla, usa una copia de self.contents
        for i in draw_list:
            self.contents.remove(i)                                     #borra los 4 items que paso la variable NUMBER
        return draw_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for x in range(num_experiments):                            #itera NUM_EXPERIMENTS times
        hatCopy = copy.deepcopy(hat)                                #Hace una copy de hat
        drawn_list = Hat.draw(hatCopy, num_balls_drawn)             #hace una lista con las NUM_BALLS_DRAWN que saco de la copia de hat
        success = True                                              
        for key, value in expected_balls.items():                   #itera por k and v dentro de EXPECTED_BALLS
            if (drawn_list.count(key) < value):                         #si el count de keys en draw_list < values en EXPECTED_BALLS
                 success = False
        if success:
            M += 1
    return M/num_experiments