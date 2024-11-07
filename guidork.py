import tkinter as tk
from tkinter import messagebox
from google_dork import GoogleDork

class GoogleDorkGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Google Dorking GUI Tool")

        tk.Label(self.window, text="Domain:").grid(row=0, column=0)
        self.domain_entry = tk.Entry(self.window, width=50)
        self.domain_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Filetype:").grid(row=1, column=0)
        self.filetype_entry = tk.Entry(self.window, width=50)
        self.filetype_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Intext:").grid(row=2, column=0)
        self.intext_entry = tk.Entry(self.window, width=50)
        self.intext_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Intitle:").grid(row=3, column=0)
        self.intitle_entry = tk.Entry(self.window, width=50)
        self.intitle_entry.grid(row=3, column=1)

        tk.Label(self.window, text="Inurl:").grid(row=4, column=0)
        self.inurl_entry = tk.Entry(self.window, width=50)
        self.inurl_entry.grid(row=4, column=1)

        self.search_button = tk.Button(self.window, text="Search", command=self.start_search)
        self.search_button.grid(row=5, column=0, columnspan=2)

        self.results_text = tk.Text(self.window, width=60, height=10)
        self.results_text.grid(row=6, column=0, columnspan=2)

    def start_search(self):

        domain = self.domain_entry.get()
        filetype = self.filetype_entry.get()
        intext = self.intext_entry.get()
        intitle = self.intitle_entry.get()
        inurl = self.inurl_entry.get()

        dork = GoogleDork(
            domain=domain,
            filetype=filetype,
            intext=intext,
            intitle=intitle,
            inurl=inurl
        )
        results = dork.search()

        self.results_text.delete(1.0, tk.END)
        if results:
            self.results_text.insert(tk.END, "Google Dorking Results:\n")
            for result in results:
                self.results_text.insert(tk.END, f"Title: {result['title']}\n")
                self.results_text.insert(tk.END, f"Link: {result['link']}\n")
                self.results_text.insert(tk.END, "-" * 80 + "\n")
        else:
            self.results_text.insert(tk.END, "No results found.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GoogleDorkGUI()
    gui.run()
