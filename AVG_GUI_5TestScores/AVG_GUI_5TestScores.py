# Thí program uses a GUI to get five test scores
# and display their sum and average
import tkinter

class TestAvg:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the frames.
        self.test_frames = []
        self.entry_widgets = []
        for i in range(5):
            test_frame = tkinter.Frame(self.main_window)
            test_label = tkinter.Label(test_frame, text=f'Enter the score for test {i+1}: ')
            test_entry = tkinter.Entry(test_frame, width=10)
            test_label.pack(side='left')
            test_entry.pack(side='left')
            self.test_frames.append(test_frame)
            self.entry_widgets.append(test_entry)

        self.avg_frame = tkinter.Frame(self.main_window)
        self.avg_label = tkinter.Label(self.avg_frame, text='Average: ')
        self.avg = tkinter.StringVar()  # To update avg_label
        self.avg_result = tkinter.Label(self.avg_frame, textvariable=self.avg)
        self.avg_label.pack(side='left')
        self.avg_result.pack(side='left')

        self.sum_frame = tkinter.Frame(self.main_window)
        self.sum_label = tkinter.Label(self.sum_frame, text='Sum: ')
        self.sum = tkinter.StringVar()  # To update sum_label
        self.sum_result = tkinter.Label(self.sum_frame, textvariable=self.sum)
        self.sum_label.pack(side='left')
        self.sum_result.pack(side='left')

        self.button_frame = tkinter.Frame(self.main_window)
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calc_avg_sum)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        for frame in self.test_frames:
            frame.pack()
        self.avg_frame.pack()
        self.sum_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    def calc_avg_sum(self):
        # Get the five test scores and store them
        # in variables.
        scores = [float(widget.get()) for widget in self.entry_widgets]

        # Calculate the sum.
        total = sum(scores)

        # Calculate the average.
        average = total / 5.0

        # Update the avg_label widget by storing
        # the value of average in the StringVar
        # object referenced by avg.
        self.avg.set('Average: {:.2f}'.format(average))

        # Update the sum_label widget by storing
        # the value of total in the StringVar
        # object referenced by sum.
        self.sum.set('{:.2f}'.format(total))

# Create an instance of the TestAvg class.
if __name__ == '__main__':
    test_avg = TestAvg()

