class Encoder:
  def __init__(self, shift):
      self.shift = shift

  def encode(self, message):
      encoded_message = ""
      for char in message:
          if char.isalpha():
              ascii_offset = 65 if char.isupper() else 97
              encoded_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
              encoded_message += encoded_char
          else:
              encoded_message += char
      return encoded_message


class Decoder:
  def __init__(self, shift):
      self.shift = shift

  def decode(self, message):
      decoded_message = ""
      for char in message:
          if char.isalpha():
              ascii_offset = 65 if char.isupper() else 97
              decoded_char = chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
              decoded_message += decoded_char
          else:
              decoded_message += char
      return decoded_message

def main():
    shift = 3  # You can adjust the shift value here

    encoder = Encoder(shift)
    decoder = Decoder(shift)

    while True:
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter a message to encode: ")
            encoded_message = encoder.encode(message)
            print("Encoded message:", encoded_message)
        elif choice == "2":
            message = input("Enter a message to decode: ")
            decoded_message = decoder.decode(message)
            print("Decoded message:", decoded_message)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()