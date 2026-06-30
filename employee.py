
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class Employeesystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll System")
        self.root.geometry("1400x720+0+0")
        self.root.config(bg="#0b0f1a")
        self.root.resizable(False, False)

        self.var_code = tk.StringVar()
        self.var_designation = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_doj = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_age = tk.StringVar()
        self.var_experience = tk.StringVar()
        self.var_gender = tk.StringVar(value="Male")
        self.var_proof = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_month = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_basic_salary = tk.StringVar()
        self.var_total_days = tk.StringVar()
        self.var_absents = tk.StringVar()
        self.var_medical = tk.StringVar()
        self.var_provident = tk.StringVar()
        self.var_conveyance = tk.StringVar()
        self.var_net_salary = tk.StringVar()

        title_bar = tk.Frame(self.root, bg="#111827", bd=0, relief=tk.FLAT)
        title_bar.place(x=0, y=0, relwidth=1, height=75)

        title_label = tk.Label(
            title_bar,
            text="Employee Payroll System",
            font=("Segoe UI", 28, "bold"),
            bg="#111827",
            fg="#f8fafc",
        )
        title_label.pack(pady=12)

        container = tk.Frame(self.root, bg="#0b0f1a")
        container.place(x=10, y=85, width=1380, height=625)

        left_panel = tk.Frame(container, bd=4, relief=tk.RIDGE, bg="#1f2937")
        left_panel.place(x=10, y=10, width=660, height=605)

        left_title = tk.Label(
            left_panel,
            text="Employee Details",
            font=("Georgia", 20, "bold"),
            bg="#2563eb",
            fg="white",
            anchor="w",
            padx=15,
        )
        left_title.place(x=0, y=0, relwidth=1, height=55)

        detail_frame = tk.Frame(left_panel, bg="#1f2937")
        detail_frame.place(x=10, y=65, width=640, height=520)

        labels = [
            "Employee Code",
            "Designation",
            "Name",
            "D.O.J",
            "D.O.B",
            "Age",
            "Experience",
            "Gender",
            "Proof ID",
            "Email",
            "Contact No",
        ]

        field_vars = [
            self.var_code,
            self.var_designation,
            self.var_name,
            self.var_doj,
            self.var_dob,
            self.var_age,
            self.var_experience,
            self.var_gender,
            self.var_proof,
            self.var_email,
            self.var_contact,
        ]

        positions = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
            (5, 0),
        ]

        for index, label_text in enumerate(labels):
            row, col = positions[index]
            lbl = tk.Label(
                detail_frame,
                text=label_text + ":",
                font=("Calibri", 14, "bold"),
                bg="#1f2937",
                fg="#e2e8f0",
            )
            lbl.grid(row=row, column=col, sticky="w", padx=12, pady=10)

            if label_text == "Gender":
                entry = ttk.Combobox(
                    detail_frame,
                    textvariable=self.var_gender,
                    values=("Male", "Female", "Other"),
                    state="readonly",
                    font=("Calibri", 13),
                    justify="center",
                )
            else:
                entry = tk.Entry(
                    detail_frame,
                    textvariable=field_vars[index],
                    font=("Calibri", 13),
                    bg="#f8fafc",
                    fg="#111827",
                    relief=tk.FLAT,
                )
            entry.grid(row=row, column=col + 1, padx=10, pady=10, sticky="ew")

        detail_frame.grid_columnconfigure(1, weight=1)
        detail_frame.grid_columnconfigure(3, weight=1)

        lbl_address = tk.Label(
            left_panel,
            text="Address :",
            font=("Calibri", 14, "bold"),
            bg="#1f2937",
            fg="#e2e8f0",
        )
        lbl_address.place(x=20, y=445)

        self.txt_address = tk.Text(
            left_panel,
            font=("Calibri", 13),
            bg="#f8fafc",
            fg="#111827",
            relief=tk.FLAT,
        )
        self.txt_address.place(x=20, y=475, width=620, height=110)

        right_panel = tk.Frame(container, bd=4, relief=tk.RIDGE, bg="#1f2937")
        right_panel.place(x=680, y=10, width=690, height=605)

        right_title = tk.Label(
            right_panel,
            text="Salary Section",
            font=("Georgia", 20, "bold"),
            bg="#0ea5e9",
            fg="white",
            anchor="w",
            padx=15,
        )
        right_title.place(x=0, y=0, relwidth=1, height=55)

        salary_frame = tk.Frame(right_panel, bg="#1f2937")
        salary_frame.place(x=10, y=65, width=670, height=240)

        salary_labels = [
            "Month",
            "Year",
            "Basic Salary",
            "Total Days",
            "Absents",
            "Medical",
            "Provident Fund",
            "Convence",
            "Net Salary",
        ]

        salary_vars = [
            self.var_month,
            self.var_year,
            self.var_basic_salary,
            self.var_total_days,
            self.var_absents,
            self.var_medical,
            self.var_provident,
            self.var_conveyance,
            self.var_net_salary,
        ]

        for index, label_text in enumerate(salary_labels):
            row = index // 2
            col = (index % 2) * 2
            lbl = tk.Label(
                salary_frame,
                text=label_text + ":",
                font=("Calibri", 14, "bold"),
                bg="#1f2937",
                fg="#e2e8f0",
            )
            lbl.grid(row=row, column=col, sticky="w", padx=12, pady=8)

            entry = tk.Entry(
                salary_frame,
                textvariable=salary_vars[index],
                font=("Calibri", 13),
                bg="#f8fafc",
                fg="#111827",
                relief=tk.FLAT,
            )
            entry.grid(row=row, column=col + 1, padx=10, pady=8, sticky="ew")

        salary_frame.grid_columnconfigure(1, weight=1)
        salary_frame.grid_columnconfigure(3, weight=1)

        button_frame = tk.Frame(right_panel, bg="#1f2937")
        button_frame.place(x=10, y=315, width=670, height=85)

        btn_calculate = tk.Button(
            button_frame,
            text="Calculate",
            command=self.calculate_salary,
            font=("Calibri", 14, "bold"),
            bg="#22c55e",
            fg="white",
            bd=0,
            width=12,
        )
        btn_calculate.grid(row=0, column=0, padx=12, pady=18)

        btn_save = tk.Button(
            button_frame,
            text="Save",
            command=self.save_salary,
            font=("Calibri", 14, "bold"),
            bg="#0ea5e9",
            fg="white",
            bd=0,
            width=12,
        )
        btn_save.grid(row=0, column=1, padx=12, pady=18)

        btn_clear = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_salary,
            font=("Calibri", 14, "bold"),
            bg="#f97316",
            fg="white",
            bd=0,
            width=12,
        )
        btn_clear.grid(row=0, column=2, padx=12, pady=18)

        receipt_panel = tk.Frame(right_panel, bd=3, relief=tk.RIDGE, bg="#1f2937")
        receipt_panel.place(x=10, y=410, width=670, height=170)

        receipt_title = tk.Label(
            receipt_panel,
            text="Salary Receipt",
            font=("Georgia", 18, "bold"),
            bg="#8b5cf6",
            fg="white",
            anchor="w",
            padx=12,
        )
        receipt_title.pack(fill=tk.X)

        self.txt_receipt = tk.Text(
            receipt_panel,
            font=("Calibri", 12),
            bg="#f8fafc",
            fg="#111827",
            relief=tk.FLAT,
        )
        self.txt_receipt.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

        btn_print = tk.Button(
            right_panel,
            text="Print",
            command=self.print_receipt,
            font=("Calibri", 14, "bold"),
            bg="#a855f7",
            fg="white",
            bd=0,
            width=12,
        )
        btn_print.place(x=520, y=580)

    def calculate_salary(self):
        try:
            basic = float(self.var_basic_salary.get() or 0)
            days = float(self.var_total_days.get() or 0)
            absent = float(self.var_absents.get() or 0)
            medical = float(self.var_medical.get() or 0)
            provident = float(self.var_provident.get() or 0)
            conveyance = float(self.var_conveyance.get() or 0)

            daily_rate = basic / max(days, 1)
            deduction = absent * daily_rate
            net_salary = basic - deduction - medical - provident + conveyance
            self.var_net_salary.set(f"{net_salary:.2f}")
            self.generate_receipt()
        except ValueError:
            messagebox.showerror("Error", "Enter valid numeric values in salary fields")

    def save_salary(self):
        address = self.txt_address.get("1.0", tk.END).strip()
        if self.var_code.get() == "" or self.var_name.get() == "" or self.var_basic_salary.get() == "":
            messagebox.showwarning("Warning", "Please enter employee and salary details before saving")
            return

        self.var_address.set(address)
        messagebox.showinfo("Saved", "Employee salary details saved successfully")

    def clear_salary(self):
        self.var_code.set("")
        self.var_designation.set("")
        self.var_name.set("")
        self.var_doj.set("")
        self.var_dob.set("")
        self.var_age.set("")
        self.var_experience.set("")
        self.var_gender.set("Male")
        self.var_proof.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0", tk.END)
        self.var_month.set("")
        self.var_year.set("")
        self.var_basic_salary.set("")
        self.var_total_days.set("")
        self.var_absents.set("")
        self.var_medical.set("")
        self.var_provident.set("")
        self.var_conveyance.set("")
        self.var_net_salary.set("")
        self.txt_receipt.delete("1.0", tk.END)

    def generate_receipt(self):
        self.txt_receipt.delete("1.0", tk.END)
        receipt_text = (
            f"Salary Receipt\n"
            f"-----------------------------\n"
            f"Employee Code : {self.var_code.get()}\n"
            f"Name : {self.var_name.get()}\n"
            f"Designation : {self.var_designation.get()}\n"
            f"Month : {self.var_month.get()} {self.var_year.get()}\n"
            f"Basic Salary : {self.var_basic_salary.get()}\n"
            f"Total Days : {self.var_total_days.get()}\n"
            f"Absents : {self.var_absents.get()}\n"
            f"Medical : {self.var_medical.get()}\n"
            f"Provident Fund : {self.var_provident.get()}\n"
            f"Convence : {self.var_conveyance.get()}\n"
            f"Net Salary : {self.var_net_salary.get()}\n"
            f"-----------------------------\n"
            f"Generated On : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        self.txt_receipt.insert(tk.END, receipt_text)

    def print_receipt(self):
        if not self.txt_receipt.get("1.0", tk.END).strip():
            messagebox.showwarning("Warning", "Generate the receipt before printing")
            return
        messagebox.showinfo("Print", "Receipt sent to printer (simulated)")


if __name__ == "__main__":
    root = tk.Tk()
    Employeesystem(root)
    root.mainloop()
