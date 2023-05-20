import paho.mqtt.client as mqtt


broker_address = "mqtt.example.com"
broker_port = 1883
username = "mynedear"
password = "your_password"


client = mqtt.Client()


client.username_pw_set(username, password)
client.connect(broker_address, broker_port)


topic = "your/topic"

message = "Hello, MQTT!"


client.publish(topic, message)


client.disconnect()
