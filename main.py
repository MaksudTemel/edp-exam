class Event:
    def __init__ (self, name, payload):
      self.name = name
      self.payload = payload

class ApplicationSubmittedEvent(Event):
  def __init__ (self "application_submitted", {"name": name, "date" : date}})

  super() .__init__ (self "application_submitted", {"name": name, "date": date} ")

class ApplicationReceivedEvent(Event):
  def __init__ (self, name, is_confirmed):
  
  super() .__init__("application_received", {"name": name, "is_confirmed": is_confirmed})

  communication_queue = []

class Applicant: 
  def __init__ (self, first_name, last_name, day_of_birth, address, phone_number):
     self.first_name = first_name
     self.last_name = last_name
     self.day_birth = day_of_birth
     self.address = address
     self.phone_number = phone_number
  
  def ask_for_application(self, date)
    event = ApplicationSubmittedEvent(self.name, date)

 communication_queue.append(event)
        print('Event', event.name, 'emitted!')

class Company:
  def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
  def handle_application_request(self, event):
        print(f"Received application for job: {event.payload['name']} on {event.payload['date']}")
        confirmation_event = 
      ApplicationReceivedEvent(event.payload["name"], is_confirmed=True)
        communication_queue.append(confirmation_event)
        print('Event', confirmation_event.name, 'emitted!')



